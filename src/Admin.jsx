import React from 'react'
import './Admin.css';

function Admin() {
    return (
        <>

            


            <h2 className='heading'>Tickets Raised</h2>

            <hr className='hline' />

            <div className="row g-4 md-4">

                <div className="col md-4">
                    <div className="container">

                       

                        <div className="text">
                            <h5 className='subheading'>Priority : </h5>
                            <p className='para1'>HIGH</p>
                        </div>

                        <div className="text">
                            <h5 className='subheading'>Ticket ID : </h5>
                            <p className='para'>01</p>
                        </div>

                        <div className="text">
                            <h5 className='subheading'>Email : </h5>
                            <p className='para'>shivansh@gmail.com</p>
                        </div>
                        <div className="text">
                            <h5 className='subheading'>Issue Title : </h5>
                            <p className='para'>Issue against SRM University</p>
                        </div>
                        <div className="text">
                            <h5 className='subheading'>Issue Description : </h5>
                            <p className='para'>Issue against SRM University</p>
                        </div>



                        <div className="d-grid gap-2 d-md-flex justify-content-md-center" id='buttons'>
                            <button className="btn btn-primary me-md-2" type="button">Resolved</button>
                            <button className="btn btn-secondary" type="button">Unresolved</button>
                        </div>
                        <div className="rect"></div>
                    </div>

                </div>

                
            </div>


        </>
    )
}

export default Admin
