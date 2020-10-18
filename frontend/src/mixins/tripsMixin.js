import axios from 'axios'
export default{
    methods:{

        deleteReport:function(id){
            axios.delete('http://localhost:8083/reports/'+id)
            .then((response) => {
                console.log(response);
              }, (error) => {
                console.log(error);
              });
        },

        // getReports: function(){
        //     axios.get('http://localhost:8083/reports/')
        //     .then(response => {this.reports = response.data})
        //     .catch((error) => console.log(error));
            
        // },
        getReportDetail: function(id){
            axios.get('http://localhost:8083/reports/?id='+id)
            .then(response => {this.report = response.data})
            .catch((error) => console.log(error));
            
        },
        updateReport:function(id, title, region, treport, distance, elevation){
            axios.put('http://localhost:8083/reports/'+id,
            {
                name:title,
                report:treport,
                elevationGain:elevation,
                distance:distance,
                region:region
            }).then((response) => {
                console.log(response);
              }, (error) => {
                console.log(error);
              });
        },

        postReport: function(title, region, treport, distance, elevation){
            
            axios.post('http://localhost:8083/reports/post',
            {
                name:title,
                report:treport,
                elevationGain:elevation,
                distance:distance,
                region:region
            }).then((response) => {
                console.log(response);
              }, (error) => {
                console.log(error);
              });
            
        },  
    }
}

