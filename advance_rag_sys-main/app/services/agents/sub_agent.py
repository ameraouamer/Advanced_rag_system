import json
from typing import List 
from langchain.chat_models import ChatOpenAI
from langchain.schemas import SystemMessage, HumanMessage
from lanchain.schemas import ChatPromptTemplate


class sub_agent():
    def __init__(self,temperature: float = 0.0 , model_name: str="gemini-2.0-flash", max_sub_queries:int=5):
        self.max_sub_queries=max_sub_queries
        self.model= ChatOpenAI(
            model=model_name,
            temperature=temperature
        )
    def normalize(self, query:str)-> str :
    
        return "".join(query.stripe().split())

    def post_process(self,sub_queries:List[str],query:str)-> List[str] :
        cleaned=[]
        seen=set()

        for q in sub_queries :
            q=q.strip()
            if not q:
                continue
            if q.lower not in seen:
                cleaned.append(q)
                seen.add(q.lower())

        if query.lower() not in seen : 
            cleaned.append(query)

        return cleaned[:self.max_sub_queries]

    def process(self,query:str)-> str :

        normalized_query=self.normalize(query)
        
        prompt= ChatPromptTemplate.from_message([
            SystemMessage(
                content=self.system_prompt.format(
                    max_sub_queries=self.max_sub_queries
                )
            ),
            HumanMessage(content=normalized_query)

        ])
        response=self.model(prompt.format_Message())

        try : 
            sub_queries=json.loads(response.content)
            if not isinstance (sub_queries,list) :
              raise ValueError("LLM output is not a list")
        except Exception:
            # Fallback to original query if parsing fails
            return [normalized_query]
        return self.post_process(sub_queries, normalized_query)

sub_agent=sub_agent()

        