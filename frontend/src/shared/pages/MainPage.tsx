import { Outlet, useNavigate } from "react-router-dom";
import { GetSessionToken } from "../tools/SessionManager";
import { useEffect } from "react";


export default function MainPage(){
    const navigate = useNavigate();
    useEffect(() => {
        if(!GetSessionToken()){
            navigate("/Login");
        }
    }, []);

    return <>
        <header>
            AntsHive
        </header>
        <div className="container">
            <div className="row">
                <div className="col-12 col-md-3">
                    <nav>
                        <ul>
                            <li><a href="/">Dashboard</a></li>
                            <li><a href="/Locations">Locations</a></li>
                            <li><a href="/Deliveries">Deliveries</a></li>
                            <li><a href="/Orders">Orders</a></li>
                        </ul>
                    </nav>
                </div>
                <div className="col-12 col-md-9">
                    <Outlet></Outlet>
                </div>
            </div>
        </div>
        

    </>;
}