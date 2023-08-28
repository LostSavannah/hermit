import { ChangeEvent, useState } from "react";
import { RemoveSessionToken, SetSessionToken } from "../tools/SessionManager";
import UsersService from "../services/UsersService";
import { useNavigate } from "react-router-dom";

export default function Login(){

    RemoveSessionToken();
    
    const [name, setName] = useState("");
    const [password, setPassword] = useState("");
    const navigate = useNavigate();

    function onNameChanged(event:ChangeEvent<HTMLInputElement>){
        setName(event.target.value);
    }

    function onPasswordChanged(event:ChangeEvent<HTMLInputElement>){
        setPassword(event.target.value);
    }

    async function onLogin(){
        const response = await (new UsersService().login({name, password}));      
        if(response.success && response.value){
            SetSessionToken(response.value);
            navigate("/");
        }
    }

    return <>
        <form>
            <div className="form-group">
                <label>Username: </label>
                <input type="text" onChange={onNameChanged}/>
            </div>
            <div className="form-group">
                <label>Password: </label>
                <input type="password" onChange={onPasswordChanged}/>
            </div>
            <div className="form-group">
                <input type="button" value="Login" onClick={onLogin}/>
            </div>
        </form>
    </>
};