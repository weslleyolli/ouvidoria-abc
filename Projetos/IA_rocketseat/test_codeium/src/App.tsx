import { useState } from 'react'
import './App.css'

type Todo = {
  id: number
  name: string
  completed: boolean
}

export function App() {

  const [todoList, setTodoList] = useState<Todo[]>([])

  return (
    <>
      <div className='App'>
        <h1>To do list</h1>
      </div>
      {todoList.map((todo) => (
        <div key={todo.id}>{todo.name}</div>
      ))}
    </>
  )
}


