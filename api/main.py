# импорт библиотек
from fastapi import FastAPI     # библиотека FastAPI
from pydantic import BaseModel  # модуль для объявления структуры данных
from api.chunks import Chunk    # модуль для работы с OpenAI

# создаем объект приложения FastAPI
app = FastAPI()

# создадим объект для работы с OpenAI
chunk = Chunk()

# класс с типами данных параметров 
class Item(BaseModel):
    name: str
    description: str
    old: int
    
# класс параметров калькулятора
class ModelCalc(BaseModel):
    a: float
    b: float        

# класс с типами данных для метода api/get_answer
class ModelAnswer(BaseModel):
    text: str    

# функция, которая будет обрабатывать запрос по пути "/"
# полный путь запроса http://127.0.0.1:8000/
@app.get("/")
def root(): 
    return {"message": "Hello FastAPI"}

# функция, которая обрабатывает запрос по пути "/about"
@app.get("/about")
def about():
    return {"message": "Страница с описанием проекта"}

# функция-обработчик с параметрами пути
@app.get("/users/{id}")
def users(id):
    return {"Вы ввели user_id": id}  

# функция-обработчик post запроса с параметрами
@app.post('/users')
def post_users(item: Item):
    return {'answer': f'Пользователь {item.name} - {item.description}, возраст {item.old} лет'}  

# функция-обработчик post запроса с параметрами
@app.post('/add')
def post_add(item:ModelCalc):
    result = item.a + item.b
    return {'result': result}

# функция обработки post запроса + декоратор 
@app.post('/api/get_answer')
def get_answer(question: ModelAnswer):
    answer = chunk.get_answer(query = question.text)
    return {'message': answer}    

# функция обработки запросов OPTIONS
@app.options("/api/get_answer")
async def options_get_answer():
    return {"Allow": "GET, POST, OPTIONS"}

# дополнение для CORS
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить запросы с любых источников
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все методы (GET, POST, OPTIONS и т.д.)
    allow_headers=["*"],  # Разрешить все заголовки
)