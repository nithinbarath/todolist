import './App.css';
import './style/style.scss'
import {
  Route,
  BrowserRouter,
  Routes,
} from "react-router-dom";
import React, { useState } from "react";
import Postlist from './components/postlist';
import Updatelist from './components/Updatelist';

function App() {
  const [notesUpdate , setNotesUpdate] = useState([]);
  return (
    <div className="App">
 	<BrowserRouter>
   <Routes>
    <Route path='/'>
      <Route index element={<Postlist
      notesUpdate={notesUpdate}
      setNotesUpdate={setNotesUpdate}
      />}/>
      <Route path='postlist' element={<Postlist
       notesUpdate={notesUpdate}
       setNotesUpdate={setNotesUpdate}
      />}/>
      <Route path='updatelist' element={<Updatelist
       notesUpdate={notesUpdate}
       setNotesUpdate={setNotesUpdate}
      />}/>
    </Route>
   </Routes>
   </BrowserRouter>
    </div>
  );
}

export default App;
