// import React from 'react';
// import ReactDOM from 'react-dom';

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA

class ExamConfigStore extends React.Component {
  constructor(){
    super();
    this.select_mode = [
      "試験モード",
      "練習モード",
    ];
    this.select_volume = [
      "10",
      "20",
      "40",
      "80",
      "100",
      "200",
    ];
    this.select_scope = [
      "全般",
      "統合",
      "スコープ",
      "タイム",
      "コスト",
      "品質",
      "コミュニケーション",
      "リスク",
      "調達",
      "ステークホルダー",
    ];
    this.select_year = [
      "2020",
      "2019",
      "2018",
      "2017",
      "2016",
      "2015",
    ];
  }

  getMode() {
    return this.select_mode;
  }

  getVolume() {
    return this.select_volume;
  }

  getScope() {
    return this.select_scope;
  }

  getYear() {
    return this.select_year;
  }
}

class ExamConfigInput extends React.Component {
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

class ExamConfigSubmit extends React.Component {
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

ReactDOM.render(
  <form className="exam-form-control" action="" method="POST">
    <ExamConfigInput block_class="select_mode" form_type="examCombo" />
    <ExamConfigInput block_class="select_volume" form_type="examCombo" />
    <ExamConfigInput block_class="select_scope" form_type="examCombo" />
    <ExamConfigInput block_class="select_year" form_type="examCombo" />
    <ExamConfigSubmit num="3" />
  </form>
  ,
  document.getElementById('wrapper')
);
