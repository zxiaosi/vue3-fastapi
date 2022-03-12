export interface addressType {
  value: string;
  label: string;
  children?: addressType[];
}

export interface formDataType {
  name: string;
  selectData: string;
  datePicker: string;
  timePicker: string;
  switchData: boolean;
  checkbox: string[];
  radio: string;
  textarea: string;
  address: any;
}
