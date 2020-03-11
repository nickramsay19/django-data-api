<template>
    <div id="data-table">
        <table  class="u-full-width">
            <thead>
                <tr>
                    <th>First name</th>
                    <th>Last name</th>
                    <th>Email</th>
                    <th>Gender</th>
                    <th>IP address</th>
                    <th>Country</th>
                    <th>Age</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="person in persons" v-bind:key="person.id">
                    <td>{{ person.first_name }}</td>
                    <td>{{ person.last_name }}</td>
                    <td>{{ person.email }}</td>
                    <td>{{ person.gender }}</td>
                    <td>{{ person.ip_address }}</td>
                    <td>{{ person.country }}</td>
                    <td>{{ person.age }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
    name: 'DataTable',
    data () {
        return {
            persons: null
        }
    },
    mounted () {
        this.$axios
            .get('http://localhost:8000/persons/')
            .then(response => (this.persons = response.data))
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    #data-table{
        height: 30em;
        overflow-y: auto;
    }
    #data-table thead th{
        position: sticky; 
        top: 0;
        background-color: white;
    }

</style>
