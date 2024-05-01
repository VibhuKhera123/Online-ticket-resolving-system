import axios from "axios";
import { prod_url } from "../../apiUrl";

export default async function createNewTicket(item){
    try {
        var res = await axios.post(`${prod_url}/ticket/predict`, item, {
            headers: {
                "Content-Type": "application/json",
                "Accept": "application/json"
            }
        });
        if(res.statusCode === 200){
            return res.data;
        }else{
            alert("An error occurred");
        }
    } catch (error) {
        console.error("An error occurred:", error);
        alert("An error occurred:", error);
    }
}