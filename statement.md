# Project Statement

**Project Title:** Real-Time Motion Detection & Activity Monitoring System  
**Name:** Vedant Sunil Patil  
**Registration Number:** 24BAI10122  
**Course:** Computer Vision

## 1. Problem Statement

Watching a camera feed continuously and noticing every movement
manually can be difficult.

This project aims to develop a simple real-time Computer Vision
system that detects movement from a live webcam. The system
compares consecutive video frames and identifies regions where
significant movement has occurred.

The detected motion is displayed using bounding boxes along with
its position and area. The system also counts motion events and
stores session information for later reference.

## 2. Scope of the Project

The project focuses on detecting motion from a single live webcam
feed using classical Computer Vision techniques.

The scope includes:

- Capturing live video from a webcam.
- Preprocessing the captured frames.
- Comparing consecutive frames to detect changes.
- Finding motion regions using contours.
- Displaying detected motion using bounding boxes.
- Showing the position and area of detected regions.
- Counting motion events.
- Recording session information in a log file.

The project is designed as a lightweight motion detection system.
It does not identify specific objects and does not use AI or
Machine Learning models.

## 3. Target Users

The project can be useful for:

- Students learning Computer Vision.
- Beginners who want to understand motion detection.
- Users who need a simple webcam-based motion monitoring system.
- Developers who want a basic starting point for motion-based
  Computer Vision applications.

## 4. High-Level Features

- Real-time motion detection using a webcam.
- Grayscale conversion and Gaussian blur.
- Frame differencing.
- Threshold-based motion detection.
- Contour-based motion region detection.
- Bounding box visualization.
- Merging of nearby motion regions.
- Center coordinate display.
- Motion area display.
- Motion event counting.
- Session duration display.
- Activity logging.

## 5. Project Goal

The main goal of this project is to demonstrate how basic
Computer Vision techniques can be combined to build a working
real-time motion detection system in a simple and modular way.
