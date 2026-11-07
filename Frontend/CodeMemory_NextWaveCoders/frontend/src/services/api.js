import axios from "axios";
const client=axios.create({baseURL:import.meta.env.VITE_API_BASE_URL||"http://localhost:8000/api/v1",timeout:15000,headers:{"Content-Type":"application/json"}});
const demo=import.meta.env.VITE_DEMO_MODE!=="false";
export async function requestOrDemo(request,fallback){try{return(await request()).data;}catch(error){if(demo)return typeof fallback==="function"?fallback(error):fallback;throw new Error(error.response?.data?.detail||error.message||"Unable to reach CodeMemory API");}}
export {client};
const demoRepositories=[
{id:"repo-1",name:"payment-service",owner:"nextwave-coders",branch:"main",language:"Python",memories:128,lastSynced:"12 min ago",status:"Synced",description:"Payment processing, reconciliation and webhook services."},
{id:"repo-2",name:"customer-portal",owner:"nextwave-coders",branch:"develop",language:"TypeScript",memories:86,lastSynced:"1 hour ago",status:"Synced",description:"Customer-facing web application and account workflows."},
{id:"repo-3",name:"notification-engine",owner:"nextwave-coders",branch:"main",language:"JavaScript",memories:42,lastSynced:"Yesterday",status:"Needs sync",description:"Event-driven email and in-app notification workers."}];
const demoMemories=[
{id:1,type:"decision",title:"Why idempotency keys are required for payment retries",repo:"payment-service",detail:"A retry could otherwise create duplicate charges when a gateway response times out. The team chose a request-scoped idempotency key stored with the transaction.",date:"Today · 10:42 AM",confidence:96,source:"PR #184 · Architecture discussion"},
{id:2,type:"bugfix",title:"Webhook signature mismatch after proxy migration",repo:"payment-service",detail:"The proxy normalized header casing. Verification was updated to use the raw request body and a case-insensitive header lookup.",date:"Yesterday · 4:18 PM",confidence:92,source:"Commit 7c1a9e2"},
{id:3,type:"caution",title:"Do not run notification workers without a deduplication key",repo:"notification-engine",detail:"A previous incident sent duplicate notifications after a worker restart. Preserve the event ID across retries.",date:"Nov 04 · 2:06 PM",confidence:89,source:"Incident note · INC-028"},
{id:4,type:"pattern",title:"Repository uses service-layer validation",repo:"customer-portal",detail:"Validation shared by multiple routes belongs in the service layer, not duplicated in individual UI components.",date:"Nov 03 · 11:30 AM",confidence:84,source:"Code analysis · src/services"}];
export const api={
getHealth:()=>requestOrDemo(()=>client.get("/health"),{status:"demo",message:"Demo mode active"}),
getDashboard:()=>requestOrDemo(()=>client.get("/dashboard/summary"),{repositories:3,memories:256,decisions:48,knowledgeCoverage:78,recentActivity:[{title:"Payment retry decision retained",repo:"payment-service",time:"12 min ago",kind:"decision"},{title:"Webhook verification fix indexed",repo:"payment-service",time:"1 hour ago",kind:"bugfix"},{title:"New repository connected",repo:"customer-portal",time:"Yesterday",kind:"sync"}]}),
getRepositories:()=>requestOrDemo(()=>client.get("/repositories"),demoRepositories),
getMemories:()=>requestOrDemo(()=>client.get("/memories"),demoMemories),
connectRepository:url=>requestOrDemo(()=>client.post("/repositories/connect",{repository_url:url}),{id:`demo-${Date.now()}`,name:url.split("/").filter(Boolean).pop()?.replace(".git","")||"new-repository",owner:"connected-workspace",branch:"main",language:"Unknown",memories:0,lastSynced:"Just now",status:"Connected",description:"Repository added in demo mode."}),
syncRepository:id=>requestOrDemo(()=>client.post(`/repositories/${id}/sync`),{status:"Sync queued",message:"Demo sync completed."}),
sendMessage:(message,repositoryId)=>requestOrDemo(()=>client.post("/chat",{message,repository_id:repositoryId||null}),{answer:"This is a demo response. In the live product, CodeMemory combines repository analysis with Hindsight Recall and Reflect results to explain the engineering context.",memories:[{title:"Idempotency prevents duplicate payment operations",source:"payment-service · PR #184",confidence:96},{title:"Webhook verification uses the raw request body",source:"payment-service · commit 7c1a9e2",confidence:92}],citations:["payment-service / docs/payment-retries.md","PR #184"],demo:true})
};
