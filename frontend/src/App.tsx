import {createBrowserRouter, RouterProvider} from 'react-router-dom';
import MainPage from './shared/pages/MainPage';
import Login from './shared/pages/Login';
import Locations from './shared/pages/Locations';
import Location from './shared/pages/Location';
import Dashboard from './shared/pages/Dashboard';
import Reservations from './shared/pages/Reservations';
import Events from './shared/pages/Events';

const router = createBrowserRouter([
  {
    path: "/",
    element: <MainPage></MainPage>,
    children: [
      {
        path: "/",
        element: <Dashboard></Dashboard>
      },
      {
        path: "Locations",
        element: <Locations></Locations>
      },
      {
        path: "Locations/:locationId",
        element: <Location></Location>
      },
      {
        path: "Reservations",
        element: <Reservations></Reservations>
      },
      {
        path: "Events",
        element: <Events></Events>
      }
    ]
  },
  {
    path: "Login",
    element: <Login></Login>
  }
])

export default function App(){
  return <RouterProvider router={router}/>;
}