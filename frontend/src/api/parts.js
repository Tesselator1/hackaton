import { HTTP } from './common'
export const Part = {
  create (config) {
    return HTTP.post('/parts/', config).then(response => {
      return response.data
    })
  },
  delete (part) {
    return HTTP.delete(`/parts/${part.id}/`)
  },
  list () {
    return HTTP.get('/parts/').then(response => {
      return response.data
    })
  }
}
