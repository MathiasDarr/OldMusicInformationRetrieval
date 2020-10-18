import axios from 'axios'
export default{
    methods:{
        uploadPost(file, filename){
            const fd = new FormData()
            fd.append('file', file, filename, fd)
            axios.post('http://localhost:8083/files',fd)
                    .then(res => { console.log(res)
            });          
        }
    }
}
