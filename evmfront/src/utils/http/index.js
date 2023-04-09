import axios from 'axios';
import { API } from '../api';

const getAllCandidates = async () => {
    return await axios.get(API + "/candidates/")
}


export const APICalls = {
    getAllCandidates
}