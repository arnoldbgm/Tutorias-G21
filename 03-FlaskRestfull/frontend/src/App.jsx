import { useState, useEffect } from "react"

const App = () => {

  // Siempre que tu quieras trabajar con tu backend debes
  // de usar useState y el useEffect

  // Con data almacenaremos la respuesta del backend (API)
  const [data, setData] = useState([]);

  useEffect(() => {
    fetchData();
  }, [])

  async function fetchData() {
    // Asi nosotros controlamos los errores
    try {
      const response = await fetch("http://127.0.0.1:5000/categorias")
      const result = await response.json()
      setData(result)
    } catch (error) {
      console.error("Ocurrio un error", error)
    }
  }

  return (
    <div>
      <h1>Lista de Categorias</h1>
      <ul>
        {
          data.map((categoria) => (
            <li key={categoria.id} >{categoria.nombre}</li>
          ))
        }
      </ul>
    </div>
  )
}

export default App
