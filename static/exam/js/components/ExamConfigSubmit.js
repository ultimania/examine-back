import React from 'react';
import ReactDOM from 'react-dom';
import logo from '../../logo.svg';
import '../../ExamConfig.css';

export default class ExamConfigSubmit extends React.Component {
  constructor(){
    super();
    this.state = {
      button1 : {
        type : "button",
        value : "クリア",
        class : "btn btn-default btn-sm",
      },
      button2 : {
        type : "submit",
        value : "再試験",
        class : "btn btn-info btn-sm",
      },
      button3 : {
        type : "submit",
        value : "試験開始",
        class : "btn btn-primary btn-sm",
      },
    };
  }

  render(){
    const items = [];
    for (let i=1; i <= this.props.num; i++){
      items.push(
        <input type={this.state["button"+i]["type"]} className={ this.state["button"+i]["class"] } value={this.state["button"+i]["value"]} />
      )
    }
    return (
      <div className="row">
        <div className="col-xs-6">
          <div className="commit_buttons">
            {items}
          </div>
        </div>
      </div>
    );
  }
}

