// /usr/local/lib/node_deps/langchain-shim.js

import { LLMChain } from "langchain/chains";
import { PromptTemplate } from "langchain/prompts";
import { ChatOpenAI } from "langchain/chat_models/openai";

export async function runChain(question) {
  const model = new ChatOpenAI({ temperature: 0 });
  const prompt = PromptTemplate.fromTemplate("Answer the following question: {question}");
  const chain = new LLMChain({ llm: model, prompt });
  const res = await chain.call({ question });
  return res.text;
}
