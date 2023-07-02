import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Header from './components/Header';
import SideNav from './components/SideNav';
import MainArea from './components/MainArea';
import Footer from './components/Footer';
import Auth from './components/Auth';
import './App.css';

class App extends React.Component {
  render() {
    return (
      <Router>
        <div className="App">
          <Header />
          <div className="main-content">
            <SideNav />
            <Switch>
              <Route path="/auth" component={Auth} />
              <Route path="/" component={MainArea} />
            </Switch>
          </div>
          <Footer />
        </div>
      </Router>
    );
  }
}

export default App;