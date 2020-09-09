import React from 'react';
import ReactDOM from 'react-dom';
import logo from '../../logo.svg';
import '../../ExamConfig.css';
import ExamConfigStore from "../stores/ExamConfigStore"


export default class ExamConfigInput extends React.Component {
  constructor(){
    super();
    this.state = {
      label : {
        select_mode : "試験モード",
        select_volume : "出題数",
        select_scope : "出題範囲",
        select_year : "出題年度",
      },
      select_item : {
        select_mode : ExamConfigStore.getMode(),
        select_volume : ExamConfigStore.getVolume(),
        select_scope : ExamConfigStore.getScope(),
        select_year : ExamConfigStore.getYear(),
      },
    };
  }

  render(){
    return (
      <div className={this.props.block_class}>
        <div className="row">
          <div className="col-xs-6 config_block">

            <div className="col-xs-6">
              <div className="exam_label">
                {this.state["label"][this.props.block_class]}
              </div>
            </div>
            <div className="col-xs-6">
              <div className={this.props.form_type}>
                { this.props.form_type == "examCombo" ? (
                  <select name={this.props.block_class} className="custom-select" >
                    {this.state["select_item"][this.props.block_class].map(value => {
                      return <option value={value}>{value}</option>
                    })}
                  </select>
                ) : (
                  <input name={this.props.block_class} type="text" />
                )}
              </div>
            </div>
          
          </div>
        </div>
      </div>
    );
  }
}

