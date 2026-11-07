import { Navigate, Route, Routes } from "react-router-dom";
import Navbar from "./components/Navbar";
import Sidebar from "./components/Sidebar";
import Home from "./pages/Home";
import Dashboard from "./pages/Dashboard";
import Chat from "./pages/Chat";
import Repository from "./pages/Repository";
import MemoryHistory from "./pages/MemoryHistory";
import Settings from "./pages/Settings";

export default function App() {
  return <div className="app-shell"><Sidebar/><div className="main-column"><Navbar/><main className="page-content">
    <Routes>
      <Route path="/" element={<Home/>}/>
      <Route path="/dashboard" element={<Dashboard/>}/>
      <Route path="/chat" element={<Chat/>}/>
      <Route path="/repositories" element={<Repository/>}/>
      <Route path="/memories" element={<MemoryHistory/>}/>
      <Route path="/settings" element={<Settings/>}/>
      <Route path="*" element={<Navigate to="/" replace/>}/>
    </Routes>
  </main><footer className="footer"><span>CODEMEMORY</span><span>Preserve the why behind every line.</span><span>Developer Knowledge Intelligence</span></footer></div></div>;
}
