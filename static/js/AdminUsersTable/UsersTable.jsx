/**
 * Created by yura on 14.04.16.
 */

var default_users = [
    {
        'First name': 'asd',
        'Last name': 'asdasd',
        'Email': 'asdasdasd'
    },
    {
        'First name': 'asd',
        'Last name': 'asdasd',
        'Email': 'asdasdasd'
    },
    {
        'First name': 'asd',
        'Last name': 'asdasd',
        'Email': 'asdasdasd'
    }
];

var UsersTable = React.createClass({
    getInitialState: function() {
        var users = this.generateUsers(default_users);

        return {
            users: users,
            users_json: default_users,
            editable_user_id: -1
        }
    },

    /////////////////////////////////////////////////////////////
    generateUsers: function(users) {
        var _this = this;

        var users_list = users.map(function(user){
            return  <tr>
                        <td>{ user['First name'] + user['Last name'] }</td>
                        <td>{ user['Email'] }</td>
                        <td>
                            <span id={ user['id'] } className="red-text cursor-pointer" onClick={ this.deleteUser }>Delete</span>
                        </td>
                    </tr>
        });

        return users_list
    },

    /////////////////////////////////////////////////////////////
    updateTable: function(users) {
        var users_list = this.generateUsers(users);

        self.setState({users: users_list})
    },

    /////////////////////////////////////////////////////////////
    getNewUsers: function() {

    },

    createUser: function() {

    },

    deleteUser: function() {

    },

    //////////////////////////////////////////////////////////////

    render: function() {
        return <table>
        <thead>
          <tr>
              <th data-field="id">Full Name</th>
              <th data-field="name">Email</th>
              <th data-field="price">Actions</th>
          </tr>
        </thead>

        <tbody>
            { this.state.users }
            <tr>
                <td>
                    <div className="input-field col-sm-6 no-padding">
                        <input id="first_name" type="email" className="validate" onChange={ this.handleInputChange } />
                        <label htmlFor="first_name">First name</label>
                    </div>
                    <div className="input-field col-sm-6 no-padding">
                        <input id="last_name" type="email" className="validate" onChange={ this.handleInputChange } />
                        <label htmlFor="last_name">Last name</label>
                    </div>
                </td>
                <td>
                    <div className="input-field">
                        <input id="email" type="email" className="validate" onChange={ this.handleInputChange } />
                        <label htmlFor="email">Email</label>
                    </div>
                </td>
                <td>
                     <a className="waves-effect waves-light btn">Add User</a>
                </td>
            </tr>
        </tbody>
      </table>
    }
});

var users_table = React.render(<UsersTable />, document.getElementById('users-table'));