import React, { Component } from "react";
import axios from "axios";


class Getlist extends Component {
    constructor(props) {
        super(props)

        this.state = {
            posts:[],
            errorMsg:''
        }
    }
    componentDidMount() {
        axios.get('http://localhost:9559/api/list/todolist')
        .then(response => {
            console.log(response)
            this.setState({posts: response.data})
        })
        .catch(error => {
            console.log(error)
            this.setState({errorMsg: 'Error retreiving data'})
        })
    }
    render() {
        const { posts, errorMsg } = this.state
        return (
            <div>
                List of posts
                {
                    posts.length ?
                    posts.map(post => <div key={post.id}>{post.notes}</div>):
                    null
                }
                {errorMsg ? <div>{errorMsg}</div> : null}
            </div>
        )
    }
}

export default Getlist

