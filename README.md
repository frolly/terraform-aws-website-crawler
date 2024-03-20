# terraform-aws-website-crawler

<a name="readme-top"></a>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

.../...

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* AWS
* Terraform
* Lambda
* Python

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

.../...

### Prerequisites

.../...

### Installation

.../...

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

In your main.tf just add this lines :

```sh
module "local_foo_module_resources" {
    source  = "frolly/website-crawler/aws"
    version = "1.0.0"
    tag_entity = "TOTO"
    tag_project = "Crawler"
    tag_environment = "dev"
    website_domain_name = "www.example.com"
    website_sitemap_index = "sitemap.xml"
    lambda_python_version = "python3.12"
}
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Add Changelog
- [x] Add back to top links
- [ ] Your idea are welcome...

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

.../...

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

François - francois.rolly@gmail.com

Project Link: [https://github.com/frolly/crawl-website-from-sitemap-to-s3](https://github.com/frolly/crawl-website-from-sitemap-to-s3.git)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

.../...

<p align="right">(<a href="#readme-top">back to top</a>)</p>
