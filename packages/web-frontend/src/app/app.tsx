import { Route, Routes, Link } from 'react-router-dom';
import { ClerkProvider, RedirectToSignIn, SignIn, SignedIn, SignedOut } from '@clerk/clerk-react';

if (!import.meta.env.VITE_CLERK_PUBLISHABLE_KEY) {
  throw new Error("Missing Publishable Key")
}

const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY;

function Home() {
  return (
    <div>
      <h1>Home</h1>
      <Link to="/dashboard">Dashboard</Link>
    </div>
  );
}

function Dasboard() {
  return (
    <div>
      <h1>Dashboard</h1>
      <Link to="/">Home</Link>
    </div>
  );
}

export function App() {
  return (
    <ClerkProvider publishableKey={clerkPubKey}>
      <Routes>
        <Route 
          path="/sign-in/*"
          element={<SignIn routing="path" path="/sign-in" />}
        />
        <Route
          path="/sign-up/*"
          element={<SignIn routing="path" path="/sign-up" />}
        />
        <Route 
          path="/" 
          element={<Home />}
        />
        <Route 
          path="/dashboard" 
          element={
            <>
              <SignedIn>
                <Dasboard />
              </SignedIn>
              <SignedOut>
                <RedirectToSignIn />
              </SignedOut>
            </>
          }
        />
      </Routes>
    </ClerkProvider>
  );
}

export default App;
