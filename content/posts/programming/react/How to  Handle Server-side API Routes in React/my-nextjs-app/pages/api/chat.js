export default async function handler(req, res) {
    if (req.method === 'POST') {
      const { text } = req.body;
  
      if (text) {
        // Simulate processing the request
        // TODO: Add secure post request here
        res.status(200).json({ message: `Server received: ${text}` });
      } else {
        res.status(400).json({ error: 'Text is required' });
      }
    } else {
      // Handle any other HTTP method
      res.setHeader('Allow', ['POST']);
      res.status(405).end(`Method ${req.method} Not Allowed`);
    }
  }
  