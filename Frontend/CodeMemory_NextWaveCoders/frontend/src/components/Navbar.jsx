import { Bell, Command, Search } from "lucide-react";
import { useNavigate } from "react-router-dom";
export default function Navbar() {
  const navigate = useNavigate();
  return <header className="topbar"><div className="breadcrumb"><span>Workspace</span><span className="slash">/</span><strong>Knowledge intelligence</strong></div>
    <div className="topbar-actions"><button className="search-trigger" onClick={()=>navigate("/chat")}><Search size={15}/><span>Search knowledge...</span><kbd><Command size={11}/> K</kbd></button><span className="topbar-divider"/><button className="icon-button" aria-label="Notifications"><Bell size={17}/><i className="notification-dot"/></button><div className="avatar">CM</div></div>
  </header>;
}
