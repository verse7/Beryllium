import axios from 'axios'

class API{

    constructor({ url }){
        this.url = url;
        this.endpoints = {}
    }

    /**
     * Create entity for a single entity's endpoints
     * @param {A entity Object} entity
     */
    createEntity(entity) {
        this.endpoints[entity.name] = this.createCRUDEndpoints(entity)
    }

    createEntities(arrayOfEntity) {
        arrayOfEntity.forEach(this.createEntity.bind(this))
    }

    /**
     * Create the basic endpoints handlers for CRUD operations
     * @param {A entity Object} entity 
     */
    createCRUDEndpoints( {name} ) {
        var endpoints = {}
        console.log(name)
        const resourceURL = `${this.url}/${name}`

        endpoints.getAll = ({ query } = {}) => axios.get(resourceURL,{ params: { query } })

        endpoints.getOne = ({ id }) => axios.get(`${resourceURL}/${id}`)

        endpoints.create = (toCreate) => axios.post(resourceURL, toCreate)

        endpoints.update = (toUpdate, config={}) => axios.put(`${resourceURL}/${toUpdate.id}`, toUpdate, config)

        endpoints.patch  = ({id}, toPatch, config={}) => axios.patch(`${resourceURL}/${id}`, toPatch, config)

        endpoints.delete = ({ id }, config={}) => axios.delete(`${resourceURL}/${id}`, config)

        return endpoints
    }

}

// export default api object with all possible endpoints
let api = new API({ url:'http://127.0.0.1:5000/api' })
api.createEntities([
    {name: 'mentors'}, 
    {name: 'mentees'}, 
    {name: 'assign'}
])
console.log(api)
export default api