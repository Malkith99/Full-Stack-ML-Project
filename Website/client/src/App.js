import './App.css';
import {BrowserRouter as Router,Route,Routes} from 'react-router-dom';
import Header from './components/Header.js';
import Home from './Pages/Home.js';
import About from './Pages/About.js';
function App() {
  return (
      <Router>
        <>
        <Routes>
            <Route path="/" element={<Home/>}></Route>
            <Route path="/about" element={<About/>}></Route>
          </Routes>
        </>
        </Router> 
  );
}

export default App;
