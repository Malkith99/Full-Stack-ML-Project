import React from 'react'
import Header from '../components/Header'
import './home.css'
import { useState } from 'react'

export default function Home() {
  const [count, setCount] = useState(0);
  const increment = () => {
    setCount(count + 1);
  }
  const decrement = () => {
    setCount(count - 1);
  }
  return (
    <>
      <div>
        <Header />
      </div>
      <div className="home">
        <h1>This is Home Page</h1>
        <span className='title'>My counter</span>
        <p className='subtitle'>The count is {count}</p>
        <button className='button' onClick={increment}>+</button>
        <button className='button' onClick={decrement}>-</button>

      </div>
    </>
  )
}

