import { useState } from 'react'
import './CreateForm.css';
import createNewTicket from './services/raiseTicket';

function CreateForm() {

    const [email, setEmail] = useState("")
    const [title, setTitle] = useState("")
    const [description, setDescription] = useState("")

    async function submit()  {
        let item = { email, title, description }
        await createNewTicket(item).then((value)=>{
            alert(value);
        })
        console.log(item);
    }

    return (
        <>
            <h2 className="heading">User Issue Form</h2>

            <hr className="hline" />

            <div className="form-container">
                <form>
                    <div className="mb-3">
                        <label htmlFor="exampleFormControlInput1" className="form-label">Email address</label>
                        <input onChange={(e) => setEmail(e.target.value)} value={email} type="email" className="form-control" placeholder="name@example.com" />
                    </div>
                    <div className="mb-3">
                        <label htmlFor="exampleFormControlInput1" className="form-label">Issue Title</label>
                        <input onChange={(e) => setTitle(e.target.value)} value={title} type="text" className="form-control" placeholder="Enter the Issue Title" />
                    </div>
                    <div className="mb-3">
                        <label htmlFor="exampleFormControlTextarea1" className="form-label">Issue Description</label>
                        <textarea onChange={(e) => setDescription(e.target.value)} value={description} className="form-control" rows="3"></textarea>
                    </div>
                    <button onClick={submit} type="submit" className="btn btn-primary">Submit</button>
                </form>
            </div>
        </>
    )
}

export default CreateForm
