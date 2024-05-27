import react from "react"
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom"
import Login from "./pages/Login"
import Register from "./pages/Register"
import NotFound from "./pages/NotFound"
import ProtectedRout from "./components/ProtectedRout"
import Connection from "./pages/Connection"
import DataCatalog from './pages/DataCatalog';
import DataDictionary from './pages/DataDictionary';


// Clear RefreshToken, AccessToken
function Logout() {
  localStorage.clear()
  return <Navigate to="/login" />
}

function RegisterAndLogout() {
  localStorage.clear()
  return <Register />
}

// Central hub, defining navigation
function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route
          path="/"
          element={
            <ProtectedRout>
              <Connection />
            </ProtectedRout>
          }
        />
        <Route path="/login" element={<Login />} />
        <Route path="/logout" element={<Logout/>}/>
        <Route path="/register" element={<RegisterAndLogout />} />
        <Route path="/catalog/tables/:connection_id" element={<DataCatalog />} />
        <Route path="/data-dictionary/:connection_id" element={<DataDictionary />} />
        <Route path="*" element={<NotFound />}></Route>
      </Routes>
    </BrowserRouter>
  )
}

export default App
