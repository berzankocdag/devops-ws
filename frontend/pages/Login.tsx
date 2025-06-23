import axios from 'axios'
import { useState } from 'react'

function Login() {
    const [user, setUser] = useState<any>(null)

    const handleLogin = async () => {
        const res = await axios.get(
            `${import.meta.env.VITE_API_BASE_URL}/users/1`
        )

        setUser(res.data)
    }

    return (
        <div>
            <button onClick={handleLogin}>Get User 1</button>
            <pre>{JSON.stringify(user, null, 2)}</pre>
        </div>
    )
}

export default Login
