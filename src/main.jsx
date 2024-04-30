import React from 'react'
import ReactDOM from 'react-dom/client'
import CreateForm from './CreateForm.jsx'
import Admin from './Admin.jsx'
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from 'react-router-dom'

ReactDOM.createRoot(document.getElementById('root')).render(
  <Router>
    <Routes>
      <Route exact path="/" element={<CreateForm/>} />
      <Route path="/admin" element={<Admin/>} />
    </Routes>
  </Router>
)
