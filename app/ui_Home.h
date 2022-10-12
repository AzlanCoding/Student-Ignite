/********************************************************************************
** Form generated from reading UI file 'HomezGqLWO.ui'
**
** Created by: Qt User Interface Compiler version 6.3.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef HOMEZGQLWO_H
#define HOMEZGQLWO_H

#include <QtCore/QLocale>
#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QFormLayout>
#include <QtWidgets/QGraphicsView>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLCDNumber>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QToolButton>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Home
{
public:
    QWidget *centralwidget;
    QVBoxLayout *verticalLayout_2;
    QGroupBox *groupBox_2;
    QVBoxLayout *verticalLayout_3;
    QFormLayout *Top;
    QHBoxLayout *horizontalLayout;
    QGraphicsView *Profile;
    QLabel *Name;
    QHBoxLayout *buttons;
    QVBoxLayout *pointsbox;
    QLabel *pointslable;
    QLCDNumber *Points;
    QToolButton *Appsb;
    QToolButton *Reviseb;
    QToolButton *Quicklinksb;
    QToolButton *button;
    QToolButton *Quicklinksb_3;
    QToolButton *Quicklinksb_2;
    QGroupBox *groupBox;

    void setupUi(QMainWindow *Home)
    {
        if (Home->objectName().isEmpty())
            Home->setObjectName(QString::fromUtf8("Home"));
        Home->setWindowModality(Qt::ApplicationModal);
        Home->setEnabled(true);
        Home->resize(800, 450);
        QSizePolicy sizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(Home->sizePolicy().hasHeightForWidth());
        Home->setSizePolicy(sizePolicy);
        Home->setMinimumSize(QSize(800, 450));
        Home->setMaximumSize(QSize(1280, 720));
        Home->setAcceptDrops(false);
        Home->setAutoFillBackground(true);
        Home->setLocale(QLocale(QLocale::English, QLocale::Singapore));
        Home->setDocumentMode(false);
        Home->setTabShape(QTabWidget::Rounded);
        Home->setDockNestingEnabled(true);
        Home->setUnifiedTitleAndToolBarOnMac(true);
        centralwidget = new QWidget(Home);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        centralwidget->setEnabled(true);
        sizePolicy.setHeightForWidth(centralwidget->sizePolicy().hasHeightForWidth());
        centralwidget->setSizePolicy(sizePolicy);
        centralwidget->setMinimumSize(QSize(800, 450));
        centralwidget->setMaximumSize(QSize(12800, 7200));
        verticalLayout_2 = new QVBoxLayout(centralwidget);
        verticalLayout_2->setSpacing(0);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        verticalLayout_2->setSizeConstraint(QLayout::SetMinimumSize);
        verticalLayout_2->setContentsMargins(0, 0, 0, 200);
        groupBox_2 = new QGroupBox(centralwidget);
        groupBox_2->setObjectName(QString::fromUtf8("groupBox_2"));
        QSizePolicy sizePolicy1(QSizePolicy::Preferred, QSizePolicy::Fixed);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(groupBox_2->sizePolicy().hasHeightForWidth());
        groupBox_2->setSizePolicy(sizePolicy1);
        groupBox_2->setMinimumSize(QSize(0, 93));
        groupBox_2->setMaximumSize(QSize(1280, 93));
        verticalLayout_3 = new QVBoxLayout(groupBox_2);
        verticalLayout_3->setSpacing(0);
        verticalLayout_3->setObjectName(QString::fromUtf8("verticalLayout_3"));
        verticalLayout_3->setContentsMargins(0, 0, 0, 0);
        Top = new QFormLayout();
        Top->setObjectName(QString::fromUtf8("Top"));
        Top->setSizeConstraint(QLayout::SetDefaultConstraint);
        Top->setFieldGrowthPolicy(QFormLayout::AllNonFixedFieldsGrow);
        Top->setRowWrapPolicy(QFormLayout::DontWrapRows);
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setSpacing(10);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        horizontalLayout->setSizeConstraint(QLayout::SetFixedSize);
        horizontalLayout->setContentsMargins(10, 10, 10, 9);
        Profile = new QGraphicsView(groupBox_2);
        Profile->setObjectName(QString::fromUtf8("Profile"));
        Profile->setMaximumSize(QSize(75, 75));
        Profile->setFrameShape(QFrame::NoFrame);
        Profile->setFrameShadow(QFrame::Plain);
        Profile->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        Profile->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        Profile->setInteractive(true);

        horizontalLayout->addWidget(Profile);

        Name = new QLabel(groupBox_2);
        Name->setObjectName(QString::fromUtf8("Name"));
        QSizePolicy sizePolicy2(QSizePolicy::Fixed, QSizePolicy::Preferred);
        sizePolicy2.setHorizontalStretch(0);
        sizePolicy2.setVerticalStretch(0);
        sizePolicy2.setHeightForWidth(Name->sizePolicy().hasHeightForWidth());
        Name->setSizePolicy(sizePolicy2);
        Name->setMinimumSize(QSize(100, 0));
        Name->setMaximumSize(QSize(120, 100));
        Name->setText(QString::fromUtf8("Azlan Chenlong Bin Mohammad Noh"));
        Name->setScaledContents(true);
        Name->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter);
        Name->setWordWrap(true);

        horizontalLayout->addWidget(Name);


        Top->setLayout(0, QFormLayout::LabelRole, horizontalLayout);

        buttons = new QHBoxLayout();
        buttons->setSpacing(0);
        buttons->setObjectName(QString::fromUtf8("buttons"));
        buttons->setSizeConstraint(QLayout::SetFixedSize);
        pointsbox = new QVBoxLayout();
        pointsbox->setSpacing(0);
        pointsbox->setObjectName(QString::fromUtf8("pointsbox"));
        pointsbox->setSizeConstraint(QLayout::SetFixedSize);
        pointsbox->setContentsMargins(-1, -1, 0, -1);
        pointslable = new QLabel(groupBox_2);
        pointslable->setObjectName(QString::fromUtf8("pointslable"));
        pointslable->setEnabled(true);
        QSizePolicy sizePolicy3(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy3.setHorizontalStretch(0);
        sizePolicy3.setVerticalStretch(0);
        sizePolicy3.setHeightForWidth(pointslable->sizePolicy().hasHeightForWidth());
        pointslable->setSizePolicy(sizePolicy3);
        pointslable->setMinimumSize(QSize(100, 45));
        pointslable->setMaximumSize(QSize(200, 45));
        QFont font;
        font.setPointSize(15);
        font.setBold(true);
        pointslable->setFont(font);
        pointslable->setAlignment(Qt::AlignCenter);

        pointsbox->addWidget(pointslable);

        Points = new QLCDNumber(groupBox_2);
        Points->setObjectName(QString::fromUtf8("Points"));
        sizePolicy3.setHeightForWidth(Points->sizePolicy().hasHeightForWidth());
        Points->setSizePolicy(sizePolicy3);
        Points->setMinimumSize(QSize(100, 45));
        Points->setMaximumSize(QSize(200, 45));

        pointsbox->addWidget(Points);


        buttons->addLayout(pointsbox);

        Appsb = new QToolButton(groupBox_2);
        Appsb->setObjectName(QString::fromUtf8("Appsb"));
        QSizePolicy sizePolicy4(QSizePolicy::Maximum, QSizePolicy::Maximum);
        sizePolicy4.setHorizontalStretch(0);
        sizePolicy4.setVerticalStretch(0);
        sizePolicy4.setHeightForWidth(Appsb->sizePolicy().hasHeightForWidth());
        Appsb->setSizePolicy(sizePolicy4);
        Appsb->setMinimumSize(QSize(10, 10));
        Appsb->setMaximumSize(QSize(200, 100));
        QFont font1;
        font1.setPointSize(12);
        font1.setBold(true);
        Appsb->setFont(font1);
        Appsb->setPopupMode(QToolButton::InstantPopup);
        Appsb->setToolButtonStyle(Qt::ToolButtonTextOnly);
        Appsb->setAutoRaise(true);
        Appsb->setArrowType(Qt::NoArrow);

        buttons->addWidget(Appsb);

        Reviseb = new QToolButton(groupBox_2);
        Reviseb->setObjectName(QString::fromUtf8("Reviseb"));
        sizePolicy4.setHeightForWidth(Reviseb->sizePolicy().hasHeightForWidth());
        Reviseb->setSizePolicy(sizePolicy4);
        Reviseb->setMinimumSize(QSize(10, 10));
        Reviseb->setMaximumSize(QSize(200, 100));
        Reviseb->setFont(font1);
        Reviseb->setPopupMode(QToolButton::InstantPopup);
        Reviseb->setToolButtonStyle(Qt::ToolButtonTextOnly);
        Reviseb->setAutoRaise(true);
        Reviseb->setArrowType(Qt::NoArrow);

        buttons->addWidget(Reviseb);

        Quicklinksb = new QToolButton(groupBox_2);
        Quicklinksb->setObjectName(QString::fromUtf8("Quicklinksb"));
        sizePolicy4.setHeightForWidth(Quicklinksb->sizePolicy().hasHeightForWidth());
        Quicklinksb->setSizePolicy(sizePolicy4);
        Quicklinksb->setMinimumSize(QSize(10, 10));
        Quicklinksb->setMaximumSize(QSize(200, 100));
        Quicklinksb->setFont(font1);
        Quicklinksb->setPopupMode(QToolButton::InstantPopup);
        Quicklinksb->setToolButtonStyle(Qt::ToolButtonTextOnly);
        Quicklinksb->setAutoRaise(true);
        Quicklinksb->setArrowType(Qt::NoArrow);

        buttons->addWidget(Quicklinksb);

        button = new QToolButton(groupBox_2);
        button->setObjectName(QString::fromUtf8("button"));
        sizePolicy4.setHeightForWidth(button->sizePolicy().hasHeightForWidth());
        button->setSizePolicy(sizePolicy4);
        button->setMinimumSize(QSize(10, 10));
        button->setMaximumSize(QSize(200, 100));
        button->setFont(font1);
        button->setPopupMode(QToolButton::InstantPopup);
        button->setToolButtonStyle(Qt::ToolButtonTextOnly);
        button->setAutoRaise(true);
        button->setArrowType(Qt::NoArrow);

        buttons->addWidget(button);

        Quicklinksb_3 = new QToolButton(groupBox_2);
        Quicklinksb_3->setObjectName(QString::fromUtf8("Quicklinksb_3"));
        sizePolicy4.setHeightForWidth(Quicklinksb_3->sizePolicy().hasHeightForWidth());
        Quicklinksb_3->setSizePolicy(sizePolicy4);
        Quicklinksb_3->setMinimumSize(QSize(10, 10));
        Quicklinksb_3->setMaximumSize(QSize(200, 100));
        Quicklinksb_3->setFont(font1);
        Quicklinksb_3->setPopupMode(QToolButton::InstantPopup);
        Quicklinksb_3->setToolButtonStyle(Qt::ToolButtonTextOnly);
        Quicklinksb_3->setAutoRaise(true);
        Quicklinksb_3->setArrowType(Qt::NoArrow);

        buttons->addWidget(Quicklinksb_3);

        Quicklinksb_2 = new QToolButton(groupBox_2);
        Quicklinksb_2->setObjectName(QString::fromUtf8("Quicklinksb_2"));
        sizePolicy4.setHeightForWidth(Quicklinksb_2->sizePolicy().hasHeightForWidth());
        Quicklinksb_2->setSizePolicy(sizePolicy4);
        Quicklinksb_2->setMinimumSize(QSize(10, 10));
        Quicklinksb_2->setMaximumSize(QSize(200, 100));
        Quicklinksb_2->setFont(font1);
        Quicklinksb_2->setPopupMode(QToolButton::InstantPopup);
        Quicklinksb_2->setToolButtonStyle(Qt::ToolButtonTextOnly);
        Quicklinksb_2->setAutoRaise(true);
        Quicklinksb_2->setArrowType(Qt::NoArrow);

        buttons->addWidget(Quicklinksb_2);


        Top->setLayout(0, QFormLayout::FieldRole, buttons);


        verticalLayout_3->addLayout(Top);


        verticalLayout_2->addWidget(groupBox_2);

        groupBox = new QGroupBox(centralwidget);
        groupBox->setObjectName(QString::fromUtf8("groupBox"));
        sizePolicy.setHeightForWidth(groupBox->sizePolicy().hasHeightForWidth());
        groupBox->setSizePolicy(sizePolicy);
        groupBox->setMinimumSize(QSize(0, 1187));

        verticalLayout_2->addWidget(groupBox);

        Home->setCentralWidget(centralwidget);

        retranslateUi(Home);

        QMetaObject::connectSlotsByName(Home);
    } // setupUi

    void retranslateUi(QMainWindow *Home)
    {
        Home->setWindowTitle(QCoreApplication::translate("Home", "Student Ignite", nullptr));
#if QT_CONFIG(accessibility)
        Home->setAccessibleName(QCoreApplication::translate("Home", "Student Ignite", nullptr));
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        Home->setAccessibleDescription(QCoreApplication::translate("Home", "Student Ignite - Home", nullptr));
#endif // QT_CONFIG(accessibility)
        pointslable->setText(QCoreApplication::translate("Home", "Points:", nullptr));
        Appsb->setText(QCoreApplication::translate("Home", "Apps", nullptr));
        Reviseb->setText(QCoreApplication::translate("Home", "Revise", nullptr));
        Quicklinksb->setText(QCoreApplication::translate("Home", "Quicklinks", nullptr));
        button->setText(QCoreApplication::translate("Home", "TBC", nullptr));
        Quicklinksb_3->setText(QCoreApplication::translate("Home", "Call", nullptr));
        Quicklinksb_2->setText(QCoreApplication::translate("Home", "Chat", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Home: public Ui_Home {};
} // namespace Ui

QT_END_NAMESPACE

#endif // HOMEZGQLWO_H
