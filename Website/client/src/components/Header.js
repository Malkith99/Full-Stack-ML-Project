import React from 'react'
import './header.css'

export default function Header() {
    return (
        <div className="header">
            {/* <p>Let us <b>Predict</b></p>
            <nav>
                    <ul>
                        <li><a href="/">Home</a></li>
                        <li><a href="/about">About</a></li>
                        <li><a href="/contact">Contact</a></li>
                    </ul>
                </nav> */}

            <div className="headerLeft">
                <p>Let us <b>Predict</b></p>
            </div>
            <div className="headerRight">
                <nav>
                    <ul>
                        <li><a href="/">Home</a></li>
                        <li><a href="/about">About</a></li>
                        <li><a href="/contact">Contact</a></li>
                    </ul>
                </nav>
            </div>
        </div>
    )
}
