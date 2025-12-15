from flask_restx import Api, Namespace, Resource, reqparse
from flask import Flask
from database_extensions import database_extensions

app = Flask(__name__)
api = Api(app)
api = Namespace('Categories', description='Categories Endpoint')
db = database_extensions("")
databaseTableName = 'categories'
databaseFieldCategoryId = 'category_id'
databaseFieldCategoryName = 'category_name'
databaseFieldParentCategoryId = 'parent_category_id'
argumentCategoryName = 'Category Name'
argumentParentCategoryId = 'Parent Category Id'

class Categories():    
    def __init__(self, databaseName):
        global db
        db = database_extensions(databaseName)

def bread_crumbs(id):
    """ Generate the categories bread crumbs eg "cat1 >> cat2 >> Cat3 >> Cat4" """
    path = []
    if id != 0:
        row = db.fetchSingleRecord(f"SELECT {databaseFieldCategoryName}, {databaseFieldParentCategoryId} FROM {databaseTableName} WHERE {databaseFieldCategoryId}='{id}'")
        if row:            
            name = row[0]
            parent_id = row[1]
            path = bread_crumbs(parent_id) + [name]
    return path

def build_category_tree(categories, parent_id='0'):
    """Recursively build a tree of categories."""
    tree = []
    for category in categories:
        if category['parent_category_id'] == parent_id:
            children = build_category_tree(categories, category['category_id'])
            category['children'] = children
            tree.append(category)
    return tree
    
@api.route('/categories', doc={"description": "Get all categories"})
class GetCategories(Resource):
    def get(self):        
        return db.fetchJson([databaseFieldCategoryId, databaseFieldCategoryName, databaseFieldParentCategoryId], databaseTableName, '', f'ORDER BY {databaseFieldCategoryName} ASC')

@api.route('/category/<string:id>/children', doc={"description": "Get children categories"})
@api.param('id', 'Category id')
class GetCategoryChildren(Resource):
    def get(self, id):
        return db.fetchJson([databaseFieldCategoryId, databaseFieldCategoryName, databaseFieldParentCategoryId], databaseTableName, f"WHERE {databaseFieldParentCategoryId}='{id}'", '')

@api.route('/category/<string:id>/breadcrumbs', doc={"description": "Get category bread crumbs"})
@api.param('id', 'Category id')
class GetCategoryBreadCrumbs(Resource):
    def get(self, id):
        return " >> ".join(bread_crumbs(id))

@api.route('/category', doc={"description": "Add a new category"}) 
class PostCategory(Resource):
    parserAdd = reqparse.RequestParser()
    parserAdd.add_argument(argumentCategoryName, type=str, help='Category Name', required=True)
    parserAdd.add_argument(argumentParentCategoryId, type=str, help='Parent Category Id', required=True)
    @api.doc(parser=parserAdd)
    def post(self):
        args = self.parserAdd.parse_args()
        categoryName = args[argumentCategoryName]
        parentCategoryId = args[argumentParentCategoryId]
        
        # Check if the category already exists
        recordExists = db.fetchSingleValue(f"SELECT COUNT(*) FROM {databaseTableName} WHERE {databaseFieldCategoryName}='{categoryName}' and {databaseFieldParentCategoryId}='{parentCategoryId}'")
        if recordExists > 0:
            return {'message': f'Category {categoryName} already exists'}, 400
        
        # Check the parent category exists
        recordExists = db.fetchSingleValue(f"SELECT COUNT(*) FROM {databaseTableName} WHERE {databaseFieldCategoryId}='{parentCategoryId}'")
        if recordExists != 1:
            return {'message': f'Parent Category {parentCategoryId} does not exists'}, 400

        newCategoryId = db.generateId()
        db.execute(f"INSERT INTO {databaseTableName} ({databaseFieldCategoryId}, {databaseFieldCategoryName}, {databaseFieldParentCategoryId}) VALUES ('{newCategoryId}', '{categoryName}', '{parentCategoryId}')") 
        return {'message': 'Category added successfully', 'category_id':newCategoryId}, 201

@api.route('/category/<category_id>') 
class UpdateCategory(Resource):
    parserUpdate = reqparse.RequestParser()
    parserUpdate.add_argument(argumentCategoryName, type=str, help='Category Name', required=True)
    parserUpdate.add_argument(argumentParentCategoryId, type=str, help='Parent Category Id', required=True)
    
    @api.doc(description="Get an existing category information")
    def get(self, category_id):
        result = db.fetchJson([databaseFieldCategoryId, databaseFieldCategoryName, databaseFieldParentCategoryId], databaseTableName, f"WHERE {databaseFieldCategoryId}='{category_id}'", '')
        if len(result) == 0:
            return {'message': f'Category {category_id} does not exists'}, 400
        return result

    @api.doc(parser=parserUpdate)
    @api.doc(description="Update an existing category")
    def put(self, category_id):
        args = self.parserUpdate.parse_args()
        categoryName = args[argumentCategoryName]
        parentCategoryId = args[argumentParentCategoryId]
        
        # Check if the category exists
        recordExists = db.fetchSingleValue(f"SELECT COUNT(*) FROM {databaseTableName} WHERE {databaseFieldCategoryId}='{category_id}'")
        if recordExists != 1:
            return {'message': f'Category {category_id} does not exist'}, 404
        
        # Check the parent category exists
        recordExists = db.fetchSingleValue(f"SELECT COUNT(*) FROM {databaseTableName} WHERE {databaseFieldCategoryId}='{parentCategoryId}'")
        if recordExists != 1:
            return {'message': f'Parent Category {parentCategoryId} does not exist'}, 400

        db.execute(f"UPDATE {databaseTableName} SET {databaseFieldCategoryName}='{categoryName}', {databaseFieldParentCategoryId}='{parentCategoryId}' WHERE {databaseFieldCategoryId}='{category_id}'") 
        return {'message': 'Category updated successfully'}, 200

    @api.doc(description="Delete an existing category")
    def delete(self, category_id):
        # Check if the category exists
        recordExists = db.fetchSingleValue(f"SELECT COUNT(*) FROM {databaseTableName} WHERE {databaseFieldCategoryId}='{category_id}'")
        if recordExists != 1:
            return {'message': f'Category {category_id} does not exist'}, 404
        
        db.execute(f"DELETE FROM {databaseTableName} WHERE {databaseFieldCategoryId}='{category_id}'") 
        return {'message': 'Category deleted successfully'}, 200

@api.route('/categories/hierarchical', doc={"description": "Get all categories in a hierarchical structure"})
class GetHierarchicalCategories(Resource):
    def get(self):
        categories = db.fetchJson([databaseFieldCategoryId, databaseFieldCategoryName, databaseFieldParentCategoryId], databaseTableName, '', f'ORDER BY {databaseFieldCategoryName} ASC')
        hierarchical_categories = build_category_tree(categories)
        return hierarchical_categories