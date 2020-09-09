import { EventEmitter } from "events";

class ExamConfigStore extends EventEmitter {
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

const examConfigStore = new ExamConfigStore;

export default examConfigStore;
