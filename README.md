# MML to DB Uploader 🚀

**Advanced MML (Man Machine Language) Processing Suite for Database Uploads**

[![Version](https://img.shields.io/badge/version-2.1.1-blue.svg)](https://github.com/hfhafan/mml_huawei_to_sql)
[![Python](https://img.shields.io/badge/python-3.8+-green.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)
[![Donate](https://img.shields.io/badge/donate-Saweria-red.svg)](https://saweria.co/HDfauzan)

## 📋 Overview

MML to DB Uploader is a professional-grade application designed for processing Huawei MML files and uploading them to database systems. Built with Python and Tkinter, it provides a modern, user-friendly interface with advanced batch processing capabilities.

## ✨ Features

- Preview

  <img width="1006" height="786" alt="image" src="https://github.com/user-attachments/assets/2d9c741f-4d1b-4f3f-95b8-00f2bdec9250" />


### 🔧 Core Functionality
- **LST CELL Processing** - Advanced parsing and enrichment of cell configuration data
- **VSWR Data Upload** - Efficient processing of VSWR measurement files
- **RET Data Upload** - Comprehensive RET subunit data handling
- **Batch Processing** - High-performance parallel processing with error handling
- **Database Integration** - MariaDB/MySQL compatibility with upsert operations

### 🎨 User Interface
- **Modern GUI** - Professional design using Color Hunt palette
- **Tab-based Layout** - Organized Upload Manager and About sections
- **Real-time Progress** - Live progress tracking and detailed logging
- **File Detection** - Automatic MML file pattern recognition
- **Responsive Design** - Adapts to different window sizes

### ⚡ Performance
- **Parallel Processing** - Multi-threaded upload operations
- **Batch Operations** - Optimized database insertions (1000 rows per batch)
- **Smart Fallback** - Row-by-row processing for failed batches
- **Memory Efficient** - Optimized data handling for large files

## 📁 File Requirements

The following files **MUST** be present in your source folder:

| File Type | Pattern | Description |
|-----------|---------|-------------|
| **LST CELL** | `LST CELL_*.txt` | Primary cell configuration data |
| **LST PDSCHCFG** | `LST PDSCHCFG_*.txt` | PDSCH configuration data |
| **LST CELLDLPCPDSCHPA** | `LST CELLDLPCPDSCHPA_*.txt` | Cell DLPC PDSCH PA data |
| **LST SECTORSPLITCELL** | `LST SECTORSPLITCELL_*.txt` | Sector split cell configuration |
| **LST SECTORSPLITGROUP** | `LST SECTORSPLITGROUP_*.txt` | Sector split group settings |
| **DSP VSWR** | `DSP VSWR_*.txt` | VSWR measurement data |
| **DSP RETSUBUNIT** | `DSP RETSUBUNIT_*.txt` | RET subunit information |

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- MariaDB/MySQL database
- Required Python packages (see requirements.txt)

### Installation
1. Clone the repository:
```bash
git clone https://github.com/hfhafan/mml_huawei_to_sql.git
cd mml_huawei_to_sql
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure database connection in `config.py`

4. Run the application:
```bash
python main.py
```

## 🎯 Usage

### 1. Select Source Folder
- Click "Browse Folder" to select your MML files directory
- Application automatically detects required file types
- Real-time file validation and status display

### 2. Start Upload Process
- Click "🚀 Start Upload Process" to begin
- Monitor progress in real-time
- View detailed logs and error reports

### 3. Monitor Progress
- Real-time batch processing updates
- Error handling with SITE_ID reporting
- Comprehensive upload summaries

## 🏗️ Architecture

### Core Components
```
MML to DB Uploader
├── GUI Layer (Tkinter)
│   ├── Upload Manager Tab
│   └── About Tab
├── Processing Engine
│   ├── File Detection
│   ├── Data Parsing
│   └── Batch Processing
└── Database Layer
    ├── Connection Management
    └── Upsert Operations
```

### Data Flow
```
MML Files → File Detection → Data Parsing → Enrichment → Batch Processing → Database Upload
```

## 🔒 Security Features

- **Credential Management** - Secure login handling
- **Database Security** - Connection encryption support
- **Error Handling** - Sensitive data protection
- **Input Validation** - File integrity checks

## 📊 Performance Metrics

| Operation | Performance | Notes |
|-----------|-------------|-------|
| **File Detection** | < 1 second | Pattern-based recognition |
| **Data Parsing** | 1000+ rows/second | Optimized pandas operations |
| **Database Upload** | 1000 rows/batch | Batch processing with fallback |
| **Memory Usage** | Optimized | Efficient DataFrame handling |

## 🛠️ Technical Details

### Technologies Used
- **Python 3.8+** - Core programming language
- **Tkinter** - GUI framework
- **Pandas** - Data manipulation
- **SQLAlchemy** - Database ORM
- **PyMySQL** - MySQL connector
- **Threading** - Parallel processing

### Database Support
- **MariaDB** - Primary target database
- **MySQL** - Full compatibility
- **Upsert Operations** - INSERT...ON DUPLICATE KEY UPDATE
- **Transaction Management** - ACID compliance

## 📝 Configuration

### Database Settings
```python
DB_NAME = "your_database"
HOST = "your_host"
USER = "your_username"
PASSWORD = "your_password"
PORT = 3306
```

### Processing Options
- **Batch Size**: Configurable (default: 1000 rows)
- **Thread Count**: Adjustable parallel processing
- **Error Handling**: Configurable retry mechanisms

## 🐛 Troubleshooting

### Common Issues
1. **File Not Found** - Ensure all required MML files are present
2. **Database Connection** - Verify credentials and network access
3. **Memory Issues** - Large files may require increased memory allocation
4. **Permission Errors** - Check file and folder access rights

### Error Reporting
- Detailed error logs with SITE_ID information
- Batch failure reporting with fallback mechanisms
- Comprehensive upload summaries

## 🤝 Contributing

We welcome contributions! Please feel free to submit issues, feature requests, or pull requests.

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Developer

**Hadi Fauzan Hanif**
- 📧 Email: [hadifauzanhanif@gmail.com](mailto:hadifauzanhanif@gmail.com)
- 📱 WhatsApp: [+62 813-5719-8294](https://wa.me/6281357198294)
- 💼 LinkedIn: [Visit Profile](https://www.linkedin.com/in/hadi-fauzan-hanif-0b407b174/)

## ☕ Support & Donations

If you find this project helpful, please consider supporting the development:

[![Saweria](https://img.shields.io/badge/Saweria-Donate-red.svg)](https://saweria.co/HDfauzan)

**Your support helps maintain and improve this project!**

## 🔮 Roadmap

- [ ] **Cloud Integration** - AWS/Azure database support
- [ ] **API Development** - RESTful API for automation
- [ ] **Mobile App** - Cross-platform mobile interface
- [ ] **Advanced Analytics** - Data visualization and reporting
- [ ] **Plugin System** - Extensible architecture

## 📈 Version History

### v2.1.1 (Current)
- ✅ Added About tab with scrolling capability
- ✅ Fixed VSWR/RET batch processing
- ✅ Improved error handling and reporting
- ✅ Enhanced GUI with modern design
- ✅ Added developer contact information

### v2.0.0
- ✅ Complete rewrite with modern architecture
- ✅ Advanced batch processing capabilities
- ✅ Professional GUI redesign
- ✅ Parallel processing implementation

### v1.0.0
- ✅ Initial release
- ✅ Basic MML processing
- ✅ Database upload functionality

---

**Made with ❤️ by Hadi Fauzan Hanif**

*For questions, support, or collaboration, don't hesitate to reach out!*
