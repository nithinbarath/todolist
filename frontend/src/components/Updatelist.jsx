import axios from "axios";
import React, {useState } from "react";

const Updatelist = ({notesUpdate}) => {
    
    
    console.log('notesUpdate = '+ notesUpdate[0])

    const [notesData, setnotesDAta] = useState({
        notes:notesUpdate[1],id:notesUpdate[0]
    })

    const changeHandler = e =>{
        const newData={...notesData}
        newData[e.target.name] = e.target.value
        setnotesDAta(newData)
        console.log("newData ="+ newData)
    }

    const updateHandle = (e) => {
        e.preventDefault()

        console.log("notesData.notes =" + notesData.notes)
        axios.put('http://localhost:9559/api/update/todolist',{id:notesData.id,notes: notesData.notes})
        .then(response => {
            console.log(response)
        })
        .catch(error => {
            console.log(error)
        })
        
    }

    return (
        <div>
            <form onSubmit={updateHandle}>
                <div>
                    Update list
                    <input
                    type="text"
                    name="notes"
                    onChange={changeHandler}
                    value={notesData.notes}
                    >
                    </input>
                </div>
                <div>
                    <button>Update list</button>
                </div>
            </form>
        </div>
    )
}

export default Updatelist;