import React from 'react';
import Header from './components/Header';
import SideNavBar from './components/SideNavBar';
import MainArea from './components/MainArea';
import Footer from './components/Footer';
import Auth from './components/Auth';
import './styles.css';

class App extends React.Component {
  render() {
    return (
      <div className="App">
        <Header />
        <SideNavBar />
        <Auth />
        <MainArea />
        <Footer />
      </div>
    );
  }
}

export default App;