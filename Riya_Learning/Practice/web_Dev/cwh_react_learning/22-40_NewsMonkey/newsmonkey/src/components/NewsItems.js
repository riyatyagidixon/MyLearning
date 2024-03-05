import React from "react";

const NewsItems = (props) => {
  let { title, description, imageUrl, newsUrl, author, date, source } = props;
  return (
    <div>
      <div className="card" >
        <div style={{
          display: 'flex',
          justifyContent: 'flex-end',
          position: 'absolute',
          right: '0'
        }
        }>
          <span className="badge rounded-pill bg-danger">
            {source}
          </span>
        </div>
        <img src={!imageUrl ? "https://cdn.dnaindia.com/sites/default/files/styles/full/public/2024/02/26/2627149-samsung-galaxy-ring.jpg" : imageUrl} className="card-img-top" alt="..." />
        <div className="card-body">
          <h5 className="card-title">{title}...</h5>
          <p className="card-text">{description}...</p>
          <p className="card-text"><small className="text-muted">By {!author ? "Unknown" : author} on {new Date(date).toUTCString()}</small></p>
          <a rel="noreferrer" href={newsUrl} target="blank" className="btn btn-sm btn-dark">
            Read More
          </a>
        </div>
      </div>
    </div >
  );

}

export default NewsItems;
