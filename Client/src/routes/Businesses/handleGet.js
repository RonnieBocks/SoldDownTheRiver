const baseURL = 'http://192.168.1.182';

async function handleGet(SessionId) {
  const url="${baseURL}/Businesses/GetBusinesses?SessionId=${SessionId}"
  console.log(url)
  const response = await fetch(url);
  const businesses = await response.json();
  return businesses;
}

export default handleGet;