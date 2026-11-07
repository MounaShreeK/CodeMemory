import { BrainCircuit, Code2, Github, LayoutDashboard, MessageSquareText, Settings2 } from "lucide-react";
import { NavLink } from "react-router-dom";
const links=[{to:"/",label:"Home",icon:Code2},{to:"/dashboard",label:"Dashboard",icon:LayoutDashboard},{to:"/chat",label:"Ask CodeMemory",icon:MessageSquareText,badge:"AI"},{to:"/repositories",label:"Repositories",icon:Github},{to:"/memories",label:"Memory timeline",icon:BrainCircuit}];
export default function Sidebar(){return <aside className="sidebar">
  <div className="brand"><div className="brand-mark"><Code2 size={21}/></div><div><div className="brand-name">code<span>memory</span></div><div className="brand-caption">DEVELOPER INTELLIGENCE</div></div></div>
  <div className="workspace-switch"><div className="workspace-icon">N</div><div className="workspace-copy"><b>NextWaveCoders</b><small>Hackathon workspace</small></div><span>⌄</span></div>
  <div className="nav-label">WORKSPACE</div><nav className="nav-links">{links.map(({to,label,icon:Icon,badge})=><NavLink key={to} to={to} end={to==="/"} className={({isActive})=>`nav-link ${isActive?"active":""}`}><Icon size={17}/><span>{label}</span>{badge&&<em>{badge}</em>}</NavLink>)}</nav>
  <div className="nav-label tools-label">SYSTEM</div><nav className="nav-links"><NavLink to="/settings" className={({isActive})=>`nav-link ${isActive?"active":""}`}><Settings2 size={17}/><span>Settings</span></NavLink></nav>
  <div className="sidebar-spacer"/><div className="memory-status"><div className="memory-status-head"><i className="pulse"/> MEMORY ENGINE <span className="live-tag">DEMO</span></div><div className="memory-status-title"><BrainCircuit size={15}/> Knowledge layer</div><p>Context retention interface ready. Connect your API to activate live memory.</p><div className="status-track"><span/></div><small>Backend connection pending</small></div>
  <div className="sidebar-user"><div className="user-avatar">N</div><div><b>NextWaveCoders</b><small>Hackathon workspace</small></div></div>
</aside>}
