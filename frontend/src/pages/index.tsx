import React, { useEffect, useState } from 'react'
import { ArrowUp, ArrowDown, ArrowLeft, ArrowRight, Power, Zap } from 'lucide-react'

function cn(...classes: string[]) {
  return classes.filter(Boolean).join(' ')
}

export default function Dashboard() {
  const [direction, setDirection] = useState<string | null>(null)
  const [boost, setBoost] = useState(false)

  const handleKeyDown = (e: KeyboardEvent) => {
    switch (e.key.toLowerCase()) {
      case 'arrowup':
        setDirection('forward')
        break
      case 'arrowdown':
        setDirection('backward')
        break
      case 'arrowleft':
        setDirection('left')
        break
      case 'arrowright':
        setDirection('right')
        break
      case 's':
        setDirection(null)
        break
      case 'a':
        setBoost(true)
        handleBoost()
        break
    }
  }

  const handleKeyUp = (e: KeyboardEvent) => {
    if (e.key.toLowerCase() === 'a') {
      setBoost(false)
    }
    if (['arrowup', 'arrowdown', 'arrowleft', 'arrowright'].includes(e.key.toLowerCase())) {
      setDirection(null)
    }
  }

  useEffect(() => {
    window.addEventListener('keydown', handleKeyDown)
    window.addEventListener('keyup', handleKeyUp)
    return () => {
      window.removeEventListener('keydown', handleKeyDown)
      window.removeEventListener('keyup', handleKeyUp)
    }
  }, [])

  const handleBoost = async () => {
    try {
      const response = await fetch('/drivefast', {
        method: 'GET',
      })
      if (response.ok) {
        console.log('GET request successful')
      } else {
        console.error('GET request failed')
      }
    } catch (error) {
      console.error('Error sending GET request:', error)
    }
  }

  return (
    <div className="min-h-screen bg-gray-900 flex items-center justify-center p-4">
      <div className="w-full max-w-3xl bg-black rounded-[40px] p-8 relative overflow-hidden">
        <div className="bg-gradient-to-b from-gray-800/50 to-gray-900/50 rounded-[32px] p-6">
          {/* Robo Car Banner */}
          <div className="text-4xl md:text-6xl font-bold text-blue-500 text-center mb-8">
            Robo Car
          </div>
          {/* Time Display */}
          <div className="text-gray-400 text-sm mb-8 text-center">
            {new Date().toLocaleTimeString()}
          </div>

          {/* Main Display */}
          <div className="relative flex justify-center items-center mb-12">
            <div className="relative z-10 text-center">
            </div>
          </div>

          {/* Controls */}
          <div className="grid grid-cols-3 gap-4 max-w-md mx-auto">
            {/* Top row */}
            <div className="col-start-2">
              <button
                onClick={() => setDirection('forward')}
                className={cn(
                  "w-full p-4 rounded-xl bg-gray-800 hover:bg-gray-700 transition-colors",
                  direction === 'forward' && "bg-blue-500 hover:bg-blue-600"
                )}
              >
                <ArrowUp className="w-6 h-6 mx-auto text-white" />
              </button>
            </div>

            {/* Middle row */}
            <button
              onClick={() => setDirection('left')}
              className={cn(
                "p-4 rounded-xl bg-gray-800 hover:bg-gray-700 transition-colors",
                direction === 'left' && "bg-blue-500 hover:bg-blue-600"
              )}
            >
              <ArrowLeft className="w-6 h-6 mx-auto text-white" />
            </button>

            <button
              onClick={() => {
                setDirection(null)
              }}
              className="p-4 rounded-xl bg-red-500 hover:bg-red-600 transition-colors"
            >
              <Power className="w-6 h-6 mx-auto text-white" />
            </button>

            <button
              onClick={() => setDirection('right')}
              className={cn(
                "p-4 rounded-xl bg-gray-800 hover:bg-gray-700 transition-colors",
                direction === 'right' && "bg-blue-500 hover:bg-blue-600"
              )}
            >
              <ArrowRight className="w-6 h-6 mx-auto text-white" />
            </button>

            {/* Bottom row */}
            <div className="col-start-2">
              <button
                onClick={() => setDirection('backward')}
                className={cn(
                  "w-full p-4 rounded-xl bg-gray-800 hover:bg-gray-700 transition-colors",
                  direction === 'backward' && "bg-blue-500 hover:bg-blue-600"
                )}
              >
                <ArrowDown className="w-6 h-6 mx-auto text-white" />
              </button>
            </div>

            {/* Boost button */}
            <div className="col-start-3">
              <button
                onMouseDown={() => {
                  setBoost(true)
                  handleBoost()
                }}
                onMouseUp={() => setBoost(false)}
                onMouseLeave={() => setBoost(false)}
                className={cn(
                  "w-full p-4 rounded-xl bg-gray-800 hover:bg-gray-700 transition-colors",
                  boost && "bg-yellow-500 hover:bg-yellow-600"
                )}
              >
                <Zap className="w-6 h-6 mx-auto text-white" />
              </button>
            </div>
          </div>

          {/* Key Controls Info */}
          <div className="mt-8 text-center text-sm text-gray-500">
            Use arrow keys to control direction | Press 'S' to stop | Hold 'A' to boost
          </div>
        </div>
      </div>
    </div>
  )
}

