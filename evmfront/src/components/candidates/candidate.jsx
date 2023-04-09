import { useCallback, useEffect, useState } from "react";
import { APICalls } from "../../utils/http";
import { API } from "../../utils/api";
import "./style.css"

const Candidate = () => {
    const [data, setData] = useState([])

    const fetchcandidates = useCallback(async() => {
        const res = await APICalls.getAllCandidates();
        console.log(res)
        if(res.status === 200){
            console.log(res)
            setData(res.data)
        }
    },[])

    useEffect(() => {

        const interval = setInterval( () => {
            fetchcandidates()
        },8000)
        return () => clearInterval(interval)
    },[fetchcandidates])

    return (
        <div className="items-center">
            {data && data.length > 0 && data.map((item, index) => {
                return <>
                    <div key={index} className="candidate-items">
                        <div className="items__inner">
                            <div className="candidate-photo">
                                <img src={API + item.photo} alt="" />
                            </div>
                            <div className="candidate-name">{item.name}</div>
                            <div className="candidate-name">Voted {item.num_votes}</div>
                        </div>
                    </div>
                </>
            })}
        </div>
    );
};

export default Candidate;