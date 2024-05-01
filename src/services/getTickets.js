import axios from "axios";
import { prod_url } from "../../apiUrl";

const getAlltickets = async()=>{
    try {
        var res = await axios.get(`${prod_url}/ticket/tickets`);
        if(res.statusCode === 200) {
            return res.data;
        }
    } catch (error) {
        alert(error.message);
        console.log(error);
    }
}

const gettLowTickets = async()=>{
    try {
        var res = await axios.get(`${prod_url}/ticket/lowtickets`);
        if(res.statusCode === 200) {
            return res.data;
        }
    } catch (error) {
        alert(error.message);
    }
}

const gettMediumTickets = async()=>{
    try {
        var res = await axios.get(`${prod_url}/ticket/mediumtickets`);
        if(res.statusCode === 200) {
            return res.data;
        }
    } catch (error) {
        alert(error.message);
    }
}
const gettHighTickets = async()=>{
    try {
        var res = await axios.get(`${prod_url}/ticket/hightickets`);
        if(res.statusCode === 200) {
            return res.data;
        }
    } catch (error) {
        alert(error.message);
    }
}
const gettCriticalTickets = async()=>{
    try {
        var res = await axios.get(`${prod_url}/ticket/criticaltickets`);
        if(res.statusCode === 200) {
            return res.data;
        }
    } catch (error) {
        alert(error.message);
    }
}

export{getAlltickets,gettLowTickets,gettMediumTickets,gettHighTickets,gettCriticalTickets}