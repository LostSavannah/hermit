import {createBrowserRouter, RouterProvider} from 'react-router-dom';
import MainPage from './shared/pages/MainPage';
import Login from './shared/pages/Login';
import Locations from './shared/pages/Locations';
import Deliveries from './shared/pages/Deliveries';
import Orders from './shared/pages/Orders';

const router = createBrowserRouter([
  {
    path: "/",
    element: <MainPage></MainPage>,
    children: [
      {
        path: "Locations",
        element: <Locations></Locations>
      },
      {
        path: "Deliveries",
        element: <Deliveries></Deliveries>
      },
      {
        path: "Orders",
        element: <Orders></Orders>
      },
    ]
  },
  {
    path: "/Login",
    element: <Login></Login>
  }
])

export default function App(){
  return <RouterProvider router={router}/>;
}