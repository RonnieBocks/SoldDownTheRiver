import { baseURL } from '../Settings';

export async function handleGet(SessionId,callback) {
  const url=`${baseURL}/Transactions/GetTransactions?SessionId=${SessionId}`
  console.log(url)
  const response = await fetch(url);
  const Transactions = await response.json();
  callback(Transactions);
}

