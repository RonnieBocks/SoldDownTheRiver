// src/routes/Transactions/handleGet.js
import { baseURL } from '../Settings';
export async function handleGetFromHumans(SessionId,TransactionId, setTransactionData) {
  const url=`${baseURL}/Transaction/GetFromHumans?TransactionId=${TransactionId}&SessionId=${SessionId}`
  console.log(url)
  const response = await fetch(url);
  const data = await response.json();

  setTransactionData(data);
}
