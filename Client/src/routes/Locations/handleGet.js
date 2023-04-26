import { baseURL } from '../Settings';

async function handleGet(SessionId) {
  const url=`${baseURL}/Locations/GetLocations?SessionId=${SessionId}`
  console.log(url)
  const response = await fetch(url);
  const locations = await response.json();
  return locations;
}

export default handleGet;
