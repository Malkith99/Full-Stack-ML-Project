import React from 'react'
import './Header.css'

export default function Header() {
    return (
        <header>
            <div class="headerLeft">
                <p>Let us <b>Predict</b></p>
            </div>
            <div class="headerRight">
                <nav>
                    <ul>
                        <li><a href="/">Home</a></li>
                        <li><a href="/about">About</a></li>
                        <li><a href="/services">Services</a></li>
                        <li><a href="/contact">Contact</a></li>
                    </ul>
                </nav>
            </div>

        </header>
    )
}
